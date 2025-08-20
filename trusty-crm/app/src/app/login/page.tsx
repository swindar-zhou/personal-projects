"use client";

import Link from "next/link";

export default function LoginPage() {
  return (
    <div className="mx-auto max-w-sm space-y-4">
      <h1 className="text-2xl font-semibold">Login</h1>
      <input className="w-full rounded-md border p-2 text-sm" placeholder="Email" />
      <input type="password" className="w-full rounded-md border p-2 text-sm" placeholder="Password" />
      <button className="w-full rounded-md bg-black text-white py-2 text-sm">Sign in</button>
      <p className="text-xs text-zinc-600">Or <Link className="underline" href="/settings">connect Gmail</Link> once available.</p>
    </div>
  );
}
