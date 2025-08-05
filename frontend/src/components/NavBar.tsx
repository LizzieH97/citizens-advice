import { DataObj } from "../types/index";

export default function NavBar({ data }: { data: DataObj[] }) {
  const buttonStyling =
    "w-36 h-16 bg-sky-700 border-2 border-gray-300 rounded-3xl text-white p-1 flex items-center justify-center text-center";
  const fixedCategories = data.map((dataObj) => {
    return dataObj.category.replaceAll("_", " ");
  });

  return (
    <nav className="bg-white border-sky-900 border-4 rounded-3xl flex flex-row items-center justify-around">
      {fixedCategories.map((cat, index) => {
        const link = cat.split(" ");
        return (
          <a href={`#${link[0]}`} key={index} className={buttonStyling}>
            {cat}
          </a>
        );
      })}
    </nav>
  );
}
