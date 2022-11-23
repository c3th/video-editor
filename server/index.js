

const express = require('express');
const fse = require('fs-extra');
const path = require('path');

const app = express();
const port = 5000;

const static = path.join(require.main.path, 'static');
const dist = path.join(require.main.path, '..', 'dist');
const build = path.join(require.main.path, '..', 'build');

function readDir() {
  const distFiles = fse.readdirSync(dist).map(file => {
    const stat = fse.statSync(path.join(dist, file));
    return {
      file,
      date: stat.birthtime,
      link: `/dist/${file}`,
      size: stat.size
    }
  });
  const buildFiles = fse.readdirSync(build).map(file => {
    const stat = fse.statSync(path.join(build, file));
    return {
      file,
      date: stat.birthtime,
      link: `/build/${file}`,
      size: stat.size
    }
  });
  return { dist: distFiles, build: buildFiles }
}

app.use('/static', express.static(static));
app.use('/build', express.static(build));
app.use('/dist', express.static(dist));

app.get('/', (req, res) => {
  return res.status(200).sendFile(
    path.join(require.main.path, 'views/index.html')
  );
});

const server = app.listen(port, () => {
  console.log('listening on port:', port);
});


const io = require('socket.io')(server);

io.on('connection', socket => {
  socket.emit('columnCreate', readDir());
});
