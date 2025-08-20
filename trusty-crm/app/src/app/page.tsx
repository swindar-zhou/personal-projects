"use client";

import Link from "next/link";
import { useQuery } from "@tanstack/react-query";
import { apiClient, API_BASE_URL } from "@/lib/api";

export default function Page() {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["health"],
    queryFn: async () => {
      const res = await apiClient.get("/healthz");
      return res.data as { ok: boolean };
    },
  });

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">Dashboard</h1>
        <span className="text-sm text-zinc-600">
          API: {isLoading ? "…" : isError ? "error" : data?.ok ? "healthy" : "unknown"} ({API_BASE_URL})
        </span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <NavCard title="Connections" description="Top alumni/contacts per company" href="/connections" />
        <NavCard title="Applications" description="Synced from Gmail labels" href="/applications" />
        <NavCard title="Tasks" description="Reminders and follow-ups" href="/tasks" disabled />
        <NavCard title="Settings" description="Import CSVs, connect Gmail" href="/settings" />
      </div>
    </div>
  );
}

function NavCard({ title, description, href, disabled }: { title: string; description: string; href: string; disabled?: boolean }) {
  const content = (
    <div className={`rounded-lg border bg-white p-4 hover:shadow-sm transition ${disabled ? "opacity-50 cursor-not-allowed" : "cursor-pointer"}`}>
      <div className="font-medium">{title}</div>
      <div className="text-sm text-zinc-600">{description}</div>
    </div>
  );
  if (disabled) return content;
  return <Link href={href}>{content}</Link>;
}
