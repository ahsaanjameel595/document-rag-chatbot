import { useState } from "react";


function ChatInput({
    onSend,
    disabled,
}) {

    const [value, setValue] =
        useState("");


    function submit(event) {

        event.preventDefault();

        if (!value.trim()) {
            return;
        }

        onSend(value);

        setValue("");

    }


    function handleKeyDown(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            submit(event);

        }

    }


    return (

        <div className="input-container">

            <form
                onSubmit={submit}
                className="chat-input"
            >

                <textarea

                    value={value}

                    onChange={(event) =>
                        setValue(event.target.value)
                    }

                    onKeyDown={handleKeyDown}

                    placeholder={
                        "Ask anything about the document..."
                    }

                    disabled={disabled}

                    rows={1}

                />


                <button
                    type="submit"
                    disabled={
                        disabled ||
                        !value.trim()
                    }
                >
                    ↑
                </button>

            </form>


            <p>
                Answers are generated from your document.
            </p>

        </div>

    );
}


export default ChatInput;