import ReactMarkdown from "react-markdown";

import SourceCard from "./SourceCard";


function ChatMessage({ message }) {

    const isUser =
        message.role === "user";


    return (

        <div
            className={
                isUser
                    ? "message-row user"
                    : "message-row assistant"
            }
        >

            <div className="avatar">

                {isUser ? "You" : "AI"}

            </div>


            <div className="message-content">

                <div className="message-bubble">

                    <ReactMarkdown>
                        {message.content}
                    </ReactMarkdown>

                </div>


                {message.sources?.length > 0 && (

                    <div className="sources">

                        <div className="sources-title">

                            📚 Sources

                        </div>


                        {message.sources.map(
                            (source, index) => (

                                <SourceCard
                                    key={index}
                                    source={source}
                                />

                            )
                        )}

                    </div>

                )}

            </div>

        </div>

    );
}


export default ChatMessage;