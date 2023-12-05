import fs from 'fs';

export function getInput(filePath: string) {
  return fs.readFileSync(filePath, { encoding: 'utf-8'})
    .split('\n')
    .filter(p => p !== '')
    .map(p => p.trim());
}

function getCardsMatches(winningNumbers: number[], yourNumbers: number[]) {
  let score = 0;
  for (let i of yourNumbers) {
    if (winningNumbers.includes(i)) {
      score += 1;
    }
  }
  return score;
}

function getScore(winningNumbers: number[], yourNumbers: number[]) {
  let score = 0;
  for (let i of yourNumbers) {
    if (winningNumbers.includes(i)) {
      score = (score === 0) ? score + 1 : score * 2;
    }
  }
  return score;
}

function parseValues(list: string[]) {
  let temp = list.filter(i => i);
  return temp.map(i => parseInt(i, 10));
}

function getNumbersFromInput(line: string) {
  let values = line.split('|');
  let winningNumbers = parseValues(values[0].split(':')[1].split(' '));
  let yourNumbers = parseValues(values[1].split(' '));
  return [winningNumbers, yourNumbers];
}

export function partOne(input: string[]) {
  let score = 0;
  for (let line of input) {
    let [winningNumbers, yourNumbers] = getNumbersFromInput(line);
    score += getScore(winningNumbers, yourNumbers);
  }
  return score;
}

export function partTwo(input: string[]) {
  let totalsArray = Array(input.length).fill(1);

  for (let idx = 0; idx < input.length; idx++) {
    let line = input[idx];
    let [winningNumbers, yourNumbers] = getNumbersFromInput(line);
    let matches = getCardsMatches(winningNumbers, yourNumbers);

    for (let j = 0; j < totalsArray[idx]; j++) {
      let offset = 1;
      for (let k = 0; k < matches; k++) {
        totalsArray[idx + offset] += 1;
        offset += 1;
      }
    }
  }

  return totalsArray.reduce((sum, value) => sum + value, 0);
}

if (require.main === module) {
  const input = getInput('input.txt');
  console.log('Part One:', partOne(input));
  console.log('Part Two:', partTwo(input));
}
