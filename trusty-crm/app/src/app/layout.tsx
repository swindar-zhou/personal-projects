import "../styles/globals.css";
import React from "react";
import { Providers } from "@/lib/providers";
import Navbar from "@/components/Navbar";

export const metadata = { title: "Trusty CRM" };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-zinc-50 text-zinc-900">
        <Providers>
          <Navbar />
          <main className="mx-auto max-w-6xl p-6">{children}</main>
        </Providers>
      </body>
    </html>
  );
}