'use client'

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Nav() {
    const path = usePathname()
    return (
        <nav style={{ borderBottom: "1px solid #999" }}>
            <ul>
                <li>
                    <strong>My web app</strong>
                </li>
            </ul>
            <ul>
                <li>
                    <Link href="/" className={`${path == '/' ? 'contrast' : ''}`}>Home</Link>
                </li>
                <li>
                    <Link href="/service-a" className={`${path == '/service-a' ? 'contrast' : ''}`}>Service A</Link>
                </li>
                <li>
                    <Link href="/service-b" className={`${path == '/service-b' ? 'contrast' : ''}`}>Service B</Link>
                </li>
            </ul>
        </nav>
    )
}