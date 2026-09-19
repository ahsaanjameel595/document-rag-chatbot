function WelcomeScreen({
    document,
    onQuestion,
}) {

    const questions = [

        "What is this document about?",

        "What are the main features?",

        "Explain the pricing plans.",

        "What are the important limitations?",

    ];


    return (

        <div className="welcome">

            <div className="welcome-icon">
                ✦
            </div>


            <h2>
                Ask your document
            </h2>


            <p>

                Ask questions about{" "}

                <strong>
                    {document?.name || "your document"}
                </strong>

                {" "}and get answers grounded in
                the document.

            </p>


            <div className="suggestions">

                {questions.map(
                    (question, index) => (

                        <button
                            key={index}
                            onClick={() =>
                                onQuestion(question)
                            }
                        >

                            {question}

                        </button>

                    )
                )}

            </div>

        </div>

    );
}


export default WelcomeScreen;