interface Props {
    path: string
}

interface BackendResponse {
    message: string
}

const Timeout = (time: number) => {
    const controller = new AbortController();
    setTimeout(() => controller.abort(), time * 1000);
    return controller;
};

export default async function Backend({ path }: Props) {
    const backendHost = process.env.BACKEND_HOST
    const backendPort = process.env.BACKEND_PORT
    let backendResponse: BackendResponse
    try {
        const data = await fetch(`http://${backendHost}:${backendPort}/${path}`, {
            signal: Timeout(1).signal,
            cache: 'no-store'
        })
        backendResponse = await data.json()
    } catch (error) {
        console.log(`Error response from ${backendHost}:${backendPort}/${path} - ${error}`)
        backendResponse = { message: "Request error" }
    }
    return <p>Response: <mark>{backendResponse.message}</mark></p>
}