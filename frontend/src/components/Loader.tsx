import { Oval } from "react-loader-spinner";

function Loader() {
    return (
        <div className="flex justify-center items-center py-4">
            <Oval
                height={30}
                width={30}
                strokeWidth={4}
                visible={true}
            />
        </div>
    );
}

export default Loader;