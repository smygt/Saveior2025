import { Link } from "@/lib/api";

interface LinkCardProps {
  link: Link;
}

export default function LinkCard({ link }: LinkCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      {link.image_url && (
        <div className="h-48 overflow-hidden">
          <img
            src={link.image_url}
            alt={link.title}
            className="w-full h-full object-cover"
          />
        </div>
      )}
      <div className="p-4">
        <h3 className="text-lg font-semibold mb-2">
          <a
            href={link.url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 hover:text-blue-800"
          >
            {link.title}
          </a>
        </h3>
        {link.short_summary && (
          <p className="text-gray-600 mb-2">{link.short_summary}</p>
        )}
        {link.source_website && (
          <p className="text-sm text-gray-500 mb-2">
            Source: {link.source_website}
          </p>
        )}
        <div className="flex flex-wrap gap-2 mt-2">
          {link.tags.map((tag) => (
            <span
              key={tag.id}
              className="px-2 py-1 bg-gray-100 text-gray-700 rounded-full text-xs"
            >
              {tag.name}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
