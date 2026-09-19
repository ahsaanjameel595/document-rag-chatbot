function SourceCard({ source }) {

    return (

        <details className="source-card">

            <summary>

                <span>
                    📄 Page {source.page}
                </span>

                <span>
                    View source
                </span>

            </summary>


            <div className="source-content">

                {source.content}

            </div>

        </details>

    );
}


export default SourceCard;