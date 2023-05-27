// In: cmd = a complete command to run in the command line shell. It is up 
//           to the user to make certain the command is properly formatted 
//           for their platform
// Out: an object with two properties:
//      out = the trimmed content the command sent to standard out.
//      err = the trimmed content the command sent to standard error.
async function sh(cmd)
{
   const { promisify } = require('util');
   const exec = promisify(require('child_process').exec);
   await exec("cd ..");
   const result = await exec(cmd);
   return {out: result.stdout.trim(), err: result.stderr.trim()};
}
module.exports = sh;