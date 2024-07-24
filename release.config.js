module.exports = {
  branches: ['main'],
  repositoryUrl: 'https://github.com/CtrlPy/hos-utility',
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    [
      '@semantic-release/changelog',
      {
        'changelogFile': 'CHANGELOG.md'
      }
    ],
    [
      '@semantic-release/exec',
      {
        'prepareCmd': 'sed -i "s/version=.*/version=\'${nextRelease.version}\',/" setup.py'
      }
    ],
    [
      '@semantic-release/git',
      {
        'assets': ['CHANGELOG.md', 'setup.py']
      }
    ],
    '@semantic-release/github'
  ]
};
