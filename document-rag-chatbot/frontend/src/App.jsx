import { useEffect, useState } from "react";

import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";


function App() {

    const [sessionId, setSessionId] = useState(
        crypto.randomUUID()
    );

    const [messages, setMessages] = useState([]);

    const [document, setDocument] = useState(null);


    useEffect(() => {

        fetch("/api/documents/")
            .then((response) => response.json())
            .then((data) => {
                setDocument(data);
            })
            .catch((error) => {
                console.error(error);
            });

    }, []);


    function newChat() {

        setSessionId(
            crypto.randomUUID()
        );

        setMessages([]);

    }


    return (

        <div className="app">

            <Sidebar
                document={document}
                onNewChat={newChat}
            />

            <ChatWindow
                sessionId={sessionId}
                messages={messages}
                setMessages={setMessages}
                document={document}
            />

        </div>

    );
}


export default App;