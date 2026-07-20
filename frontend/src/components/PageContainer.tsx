import type { ReactNode } from "react";

interface Props {
    title: string;
    children: ReactNode;
}

function PageContainer({ title, children }: Props) {
    return (
        <div className="max-w-7xl mx-auto px-6 py-8">

            <h1 className="text-3xl font-bold mb-8">
                {title}
            </h1>

            {children}

        </div>
    );
}

export default PageContainer;