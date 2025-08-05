"use client";

import { Source, DataObj } from "../types/index";

type Props = { data: DataObj };

export default function Content({ data }: Props) {
  // TODO: Implement the content component to render out the content and sources
  return (
    <div className="border-2 border-gray-300 p-4 rounded-md">
      Individual content and sources should go in this component
    </div>
  );
}
