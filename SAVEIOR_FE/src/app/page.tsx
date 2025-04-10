export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        Welcome to Saveior
      </h1>
      <p className="text-lg text-gray-600 mb-6">
        Your modern link management solution
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Placeholder for links/folders */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Quick Access</h2>
          <p className="text-gray-600">Your most used links will appear here</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Recent Links</h2>
          <p className="text-gray-600">
            Your recently added links will appear here
          </p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Folders</h2>
          <p className="text-gray-600">
            Your organized folders will appear here
          </p>
        </div>
      </div>
    </div>
  );
}
