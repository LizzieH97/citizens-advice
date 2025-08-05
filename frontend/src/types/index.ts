export type Source = {
  id: string;
  title: string;
  source: string;
  favicon: string;
};

export type DataObj = {
  category: string;
  content: string;
  sources: Source[];
};
