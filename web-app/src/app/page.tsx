import Link from "next/link";

export default function Home() {
  return (
    <>
      <h1>Welcome!</h1>
      <p>Please check out the <Link href="/service-a">Service A</Link> and <Link href="/service-b">Service B</Link> pages.</p>
    </>
  );
}
