/**
 * @param {string[]} logs
 * @return {string[]}
 */
const reorderLogFiles = logs => {
  const letters = [];
  const digits = [];
  logs.forEach(v => isNaN(v.split(' ')[1]) ? letters.push(v) : digits.push(v));

  return letters.sort((a, b) => {
    const letterLogA = a.split(' ').slice(1).join(' ');
    const letterLogB = b.split(' ').slice(1).join(' ');
    return letterLogA === letterLogB
      ? a.split(' ')[0].localeCompare(b.split(' ')[0])
      : letterLogA.localeCompare(letterLogB);
  }).concat(digits);
};