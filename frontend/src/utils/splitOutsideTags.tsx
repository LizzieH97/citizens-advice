export const SplitOutsideTags = (html: string): [string, string] => {
  const regex = /(?<!<[^>]*):/g;

  let match;
  while ((match = regex.exec(html))) {
    const index = match.index;
    const before = html.slice(0, index + 1);
    const after = html.slice(index + 1);
    return [before, after];
  }

  return [html, ""];
};
