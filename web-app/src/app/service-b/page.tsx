import Backend from '@/app/ui/backend'

export default async function Page() {
  return (
    <>
      <h1>Service B</h1>
      <Backend path="service-b" />
    </>
  )
}