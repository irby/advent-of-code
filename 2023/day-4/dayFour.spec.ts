import { getInput, partOne, partTwo } from "./dayFour";

const input = getInput('sample.txt');

describe('part 1', () => {
  describe('when input is supplied', () => {
    const result = partOne(input);
    it('should return expected value', () => {
      expect(result).toBe(13);
    });
  });
});

describe('part 2', () => {
  describe('when input is supplied', () => {
    const result = partTwo(input);
    it('should return expected value', () => {
      expect(result).toBe(30);
    });
  });
});
