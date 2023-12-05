import { InitialOptionsTsJest } from 'ts-jest/dist/types';

const config: InitialOptionsTsJest = {
  testMatch: ['**.spec.ts'],
  transform: {
    '^.+\\.tsx?$': [
      'esbuild-jest',
      {
        sourcemap: true,
        loaders: {
          '.spec.ts': 'tsx',
        },
      },
    ],
  },
  clearMocks: true,
  testEnvironment: 'node',
  rootDir: '.',
  roots: ['<rootDir>'],
  collectCoverage: false
};

export default config;
