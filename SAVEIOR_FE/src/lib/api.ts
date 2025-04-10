const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

if (!API_BASE_URL) {
  throw new Error("NEXT_PUBLIC_API_URL is not defined");
}

export interface Link {
  id: number;
  url: string;
  title: string;
  short_summary?: string;
  long_summary?: string;
  source_website?: string;
  image_url?: string;
  created_at: string;
  updated_at: string;
  folders: Folder[];
  tags: Tag[];
}

export interface Folder {
  id: number;
  name: string;
  parent_id?: number;
  created_at: string;
  updated_at: string;
}

export interface Tag {
  id: number;
  name: string;
  is_auto_generated: boolean;
  created_at: string;
}

// API Client
export const api = {
  // Links
  getLinks: async (): Promise<Link[]> => {
    const response = await fetch(`${API_BASE_URL}/links/`);
    return response.json();
  },

  createLink: async (
    link: Omit<Link, "id" | "created_at" | "updated_at" | "folders" | "tags">
  ): Promise<Link> => {
    const response = await fetch(`${API_BASE_URL}/links/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(link),
    });
    return response.json();
  },

  // Folders
  getFolders: async (): Promise<Folder[]> => {
    const response = await fetch(`${API_BASE_URL}/folders/`);
    return response.json();
  },

  createFolder: async (
    folder: Omit<Folder, "id" | "created_at" | "updated_at">
  ): Promise<Folder> => {
    const response = await fetch(`${API_BASE_URL}/folders/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(folder),
    });
    return response.json();
  },

  // Tags
  getTags: async (): Promise<Tag[]> => {
    const response = await fetch(`${API_BASE_URL}/tags/`);
    return response.json();
  },

  createTag: async (tag: Omit<Tag, "id" | "created_at">): Promise<Tag> => {
    const response = await fetch(`${API_BASE_URL}/tags/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(tag),
    });
    return response.json();
  },
};
