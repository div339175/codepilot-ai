import type { IconType } from "react-icons";

interface Props {
    title: string;
    value: number;
    icon: IconType;
}

function StatCard({
    title,
    value,
    icon: Icon,
}: Props) {
    return (
        <div className="bg-white rounded-2xl shadow p-6 flex items-center justify-between">

            <div>

                <p className="text-gray-500">

                    {title}

                </p>

                <h2 className="text-3xl font-bold mt-2">

                    {value}

                </h2>

            </div>

            <Icon
                className="text-blue-600"
                size={40}
            />

        </div>
    );
}

export default StatCard;