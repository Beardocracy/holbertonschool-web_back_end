export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    return array.map((element) => element.id);
  }
  return [];
}
