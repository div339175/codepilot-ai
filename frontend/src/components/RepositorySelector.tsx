import { useEffect, useState } from "react";

import { getRepositories } from "../api/repository";

interface Props {

    value: string;

    onChange: (value: string) => void;

}

function RepositorySelector({

    value,

    onChange

}: Props) {

    const [repositories, setRepositories] = useState<string[]>([]);

    useEffect(() => {

        async function load() {

            try {

                const data = await getRepositories();

                setRepositories(data.repositories);

            } catch (err) {

                console.error(err);

            }

        }

        load();

    }, []);

    return (

        <select

            value={value}

            onChange={(e)=>onChange(e.target.value)}

            className="border rounded-lg w-full p-3"

        >

            <option value="">

                Select Repository

            </option>

            {repositories.map((repo)=>(

                <option

                    key={repo}

                    value={repo}

                >

                    {repo}

                </option>

            ))}

        </select>

    );

}

export default RepositorySelector;