"use client";

import React from "react";

export default function SettingsPage() {
  const [csvPreview, setCsvPreview] = React.useState<string | null>(null);

  function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      const text = String(reader.result || "");
      const lines = text.split(/\r?\n/).filter(Boolean);
      setCsvPreview(`${lines.length} rows detected`);
    };
    reader.readAsText(file);
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Settings</h1>

      <section className="space-y-2">
        <h2 className="text-lg font-medium">CSV Import</h2>
        <div className="rounded-lg border bg-white p-4 space-y-3">
          <input type="file" accept=".csv" onChange={handleFileChange} />
          <div className="text-sm text-zinc-600">{csvPreview ?? "Upload a LinkedIn or alumni CSV to import contacts."}</div>
        </div>
      </section>

      <section className="space-y-2">
        <h2 className="text-lg font-medium">Gmail</h2>
        <div className="rounded-lg border bg-white p-4 space-y-3">
          <button className="inline-flex items-center rounded-md bg-black px-3 py-2 text-sm text-white disabled:opacity-50" disabled>
            Connect Gmail (coming soon)
          </button>
          <div className="text-sm text-zinc-600">We will request read-only access to specific labels, not your entire inbox.</div>
        </div>
      </section>
    </div>
  );
}
