import parse from "html-react-parser";
import { DataObj } from "../types/index";

function decodeHtml(html: string) {
  const parser = new DOMParser();
  return (
    parser.parseFromString(html, "text/html").documentElement.textContent || ""
  );
}
export default function Content({ data }: { data: DataObj }) {
  const decoded = decodeHtml(data.content);

  const cleanedContent = decoded.replaceAll("<b>", "<br/><b>");

  const match = cleanedContent.match(/^([\s\S]*?):/);
  const matchedTitle = match?.[0] || "";
  const title = matchedTitle;
  const body = cleanedContent.slice(matchedTitle.length);

  return (
    <div className="border-2 border-gray-300 p-4 bg-sky-700 rounded-md">
      <h1 className="text-white text-2xl mb-2">{parse(title)}</h1>
      <div className="text-base text-white">{parse(body)}</div>

      {data.sources.map((source) => (
        <section
          key={source.id}
          className="flex flex-row items-center justify-start p-4 m-2 bg-white border-2 border-sky-900 rounded-3xl text-black text-xl w-3/4"
        >
          {source.title}
          <a
            href={source.source}
            className="relative w-16 h-16 block ml-4"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src={source.favicon}
              className="absolute inset-1 w-auto h-auto object-cover"
              alt="favicon"
            />
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 translate-x-[3px] -translate-y-1/2 text-xs text-white font-bold text-center">
              CLICK HERE
            </div>
          </a>
        </section>
      ))}
    </div>
  );
}
