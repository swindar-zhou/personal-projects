"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const NAV_ITEMS = [
  { href: "/", label: "Dashboard" },
  { href: "/connections", label: "Connections" },
  { href: "/applications", label: "Applications" },
  { href: "/settings", label: "Settings" },
];

export default function Navbar() {
  const pathname = usePathname();
  return (
    <header className="border-b bg-white">
      <div className="mx-auto max-w-6xl px-6 h-14 flex items-center justify-between">
        <Link href="/" className="font-semibold">Trusty CRM</Link>
        <nav className="flex gap-4">
          {NAV_ITEMS.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className={`text-sm ${pathname === item.href ? "text-black font-medium" : "text-zinc-600 hover:text-zinc-900"}`}
            >
              {item.label}
            </Link>
          ))}
        </nav>
        <Link href="/login" className="text-sm text-zinc-600 hover:text-zinc-900">Login</Link>
      </div>
    </header>
  );
} 