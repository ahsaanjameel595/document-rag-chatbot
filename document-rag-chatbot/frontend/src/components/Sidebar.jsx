function Sidebar({
    document,
    onNewChat,
}) {

    return (

        <aside className="sidebar">

            <div>

                <div className="logo">
                    <div className="logo-icon">
                        ✦
                    </div>

                    <div>
                        <h2>DocuAI</h2>
                        <span>RAG Assistant</span>
                    </div>
                </div>


                <button
                    className="new-chat"
                    onClick={onNewChat}
                >
                    + New Chat
                </button>


                <div className="sidebar-section">

                    <p className="section-title">
                        DOCUMENT
                    </p>

                    <div className="document-card">

                        <div className="pdf-icon">
                            PDF
                        </div>

                        <div>

                            <strong>
                                {document?.name || "Loading..."}
                            </strong>

                            <span>
                                PDF Document
                            </span>

                        </div>

                    </div>

                </div>


                <div className="sidebar-section">

                    <p className="section-title">
                        CAPABILITIES
                    </p>

                    <div className="capability">
                        ✓ Document Q&A
                    </div>

                    <div className="capability">
                        ✓ Source citations
                    </div>

                    <div className="capability">
                        ✓ Context-aware answers
                    </div>

                </div>

            </div>


            <div className="sidebar-footer">

                <div className="status-dot"></div>

                <span>
                    RAG System Online
                </span>

            </div>

        </aside>

    );
}


export default Sidebar;