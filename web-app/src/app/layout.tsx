import type { Metadata } from "next";
import '@/app/static/pico.min.css';

import Nav from '@/app/ui/nav'

export const metadata: Metadata = {
  title: "My web app",
  description: "Web app for app mod workshop",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <header className="container-fluid">
          <Nav />
        </header>
        <main className="container-fluid">
          {children}
        </main>
      </body>
    </html>
  );
}
