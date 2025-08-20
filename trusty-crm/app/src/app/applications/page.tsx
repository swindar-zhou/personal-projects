"use client";

export default function ApplicationsPage() {
  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-semibold">Applications</h1>
      <div className="rounded-lg border bg-amber-50 p-4 text-sm text-amber-900">
        Connect your Gmail (read-only, label scoped) to auto-detect applications.
      </div>
      <div className="rounded-lg border bg-white p-8 text-center text-zinc-600">No applications yet.</div>
    </div>
  );
}
