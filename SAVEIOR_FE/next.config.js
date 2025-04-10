/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "standalone",
  images: {
    domains: [
      "fastapi.tiangolo.com",
      "reactjs.org",
      "www.tripadvisor.com",
      "www.allrecipes.com",
    ],
  },
  experimental: {
    serverActions: true,
  },
};

module.exports = nextConfig;
