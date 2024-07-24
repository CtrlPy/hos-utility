module.exports = {
  branches: ['main'],
  repositoryUrl: 'https://github.com/CtrlPy/hos-utility',
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    '@semantic-release/changelog',
    [
      '@semantic-release/exec',
      {
        prepareCmd: 'echo ${nextRelease.version} > VERSION.txt'
      }
    ],
    [
      '@semantic-release/git',
      {
        assets: ['VERSION.txt', 'CHANGELOG.md', 'setup.py']
      }
    ],
    '@semantic-release/github',
    'semantic-release-pypi'
  ]
};
