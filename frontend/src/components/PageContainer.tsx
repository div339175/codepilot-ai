import type { ReactNode } from "react";

interface Props {
    title: string;
    children: ReactNode;
    action?: ReactNode;
}

function PageContainer({ title, children, action }: Props) {
    return (
        <div className="max-w-7xl mx-auto px-6 py-8">

            <div className="flex items-center justify-between mb-8">

                <h1 className="text-3xl font-bold">
                    {title}
                </h1>

                {action}

            </div>

            {children}

        </div>
    );
}

export default PageContainer;