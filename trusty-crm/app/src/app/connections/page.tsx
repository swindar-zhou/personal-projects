"use client";

export default function ConnectionsPage() {
  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-semibold">Connections</h1>
      <div className="flex gap-2">
        <input className="w-full rounded-md border p-2 text-sm" placeholder="Search contacts or companies..." />
        <button className="rounded-md border px-3 py-2 text-sm bg-white">Import CSV</button>
      </div>
      <div className="rounded-lg border bg-white p-8 text-center text-zinc-600">
        No connections yet. Import a LinkedIn/alumni CSV in Settings.
      </div>
    </div>
  );
}
