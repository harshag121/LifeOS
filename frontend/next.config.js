/** @type {import('next').NextConfig} */
const API_URL = process.env.API_URL || 'http://localhost:8000'
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${API_URL}/api/:path*`,
      },
    ]
  },
}
module.exports = nextConfig
