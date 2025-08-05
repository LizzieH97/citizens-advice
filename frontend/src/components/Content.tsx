import parse from "html-react-parser";
import { DataObj } from "../types/index";
import { SplitOutsideTags } from "@/utils/splitOutsideTags";

export default function Content({ data }: { data: DataObj }) {
  const [title, body] = SplitOutsideTags(data.content);
  const inlineBolds = ["debt advice"];
  const pattern = new RegExp(`<b>(?!(${inlineBolds.join("|")})<\\/b>)`, "g");
  const lineBreakBody = body.replace(pattern, "<br/><b>");
  const fixedSourceTitle = title.replaceAll(
    "href",
    'className="text-decoration-line text-emerald-400 text-2xl" href'
  );
  const fixedSourceBody = lineBreakBody.replaceAll(
    "href",
    'className="text-decoration-line text-emerald-400 text-lg" href'
  );
  return (
    <div className="border-2 border-gray-300 p-4 bg-sky-700 rounded-md">
      <div className="text-white text-2xl px-2">{parse(fixedSourceTitle)}</div>
      <div className="text-lg text-white px-2">{parse(fixedSourceBody)}</div>

      {data.sources.map((source) => (
        <section
          key={source.id}
          className="flex flex-row items-center justify-around px-4 py-2 my-2 bg-white border-2 border-sky-900 rounded-3xl text-sky-900 text-lg w-1/2"
        >
          <div className="w-3/4">{source.title}</div>

          <a
            href={source.source}
            className="relative w-20 h-20 block ml-4"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src={source.favicon}
              className="absolute inset-0 w-auto h-auto object-cover"
              alt="favicon"
            />
            <div className="absolute top-1/3 left-1/3 -translate-x-1/3 -translate-y-1/3 text-xs text-white font-bold text-center pr-2">
              click here
            </div>
          </a>
        </section>
      ))}
    </div>
  );
}
