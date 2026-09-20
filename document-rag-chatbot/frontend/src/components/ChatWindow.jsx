import { useState } from "react";

import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";
import WelcomeScreen from "./WelcomeScreen";


function ChatWindow({
    sessionId,
    messages,
    setMessages,
    document,
}) {

    const [loading, setLoading] = useState(false);


    async function sendMessage(question) {

        if (!question.trim() || loading) {
            return;
        }


        setMessages((previous) => [

            ...previous,

            {
                role: "user",
                content: question,
            },

        ]);


        setLoading(true);
try {
    const response = await fetch(
        "https://devoted-manifestation-production-927e.up.railway.app/api/chat/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                question,
                session_id: sessionId,
            }),
        }
    );


            const data =
                await response.json();


            setMessages((previous) => [

                ...previous,

                {
                    role: "assistant",
                    content: data.answer,
                    sources: data.sources || [],
                },

            ]);

        }

        catch (error) {

            console.error(error);

            setMessages((previous) => [

                ...previous,

                {
                    role: "assistant",
                    content:
                        "Sorry, something went wrong. Please try again.",
                },

            ]);

        }

        finally {

            setLoading(false);

        }

    }


    return (

        <main className="chat-area">

            <header className="topbar">

                <div>

                    <h1>
                        {document?.name ||
                            "Document Assistant"}
                    </h1>

                    <span>
                        AI-powered document Q&A
                    </span>

                </div>


                <div className="online-status">

                    <span></span>

                    AI Ready

                </div>

            </header>


            <div className="messages">

                {messages.length === 0 ? (

                    <WelcomeScreen
                        document={document}
                        onQuestion={sendMessage}
                    />

                ) : (

                    messages.map(
                        (message, index) => (

                            <ChatMessage
                                key={index}
                                message={message}
                            />

                        )
                    )

                )}


                {loading && (

                    <div className="typing">

                        <span></span>
                        <span></span>
                        <span></span>

                        Thinking...

                    </div>

                )}

            </div>


            <ChatInput
                onSend={sendMessage}
                disabled={loading}
            />

        </main>

    );
}


export default ChatWindow;