<%*
const mdc = app.metadataCache
const file = tp.file.find_tfile(tp.file.title)
const {update} = app.plugins.plugins["metaedit"].api
let candidates = app.vault.getMarkdownFiles().filter(x => "frontmatter" in mdc.getFileCache(x)).filter(x => x.basename !== tp.file.title)
candidates = candidates.filter(x => !x.path.startsWith("Templates"))

candidates = candidates.filter(x => ("source" in mdc.getFileCache(x).frontmatter))
candidates = candidates.filter(x => mdc.getFileCache(x).frontmatter.source !== null)

console.log(`The following are all candidates containing a non-null source field: `)
console.log(candidates)

let sources = []
candidates.forEach(
	function (e) {
		let source = mdc.getFileCache(e).frontmatter.source
		if (Array.isArray(source)) {
			source.forEach(x => this.push(x), this)
		} else {
			this.push(source)
		}
	}, sources
)

let alias = await tp.system.prompt("Insert Class Alias...", "", false, false)

sources = sources.filter(x => x["source-alias"] === alias)

console.log(`The following are all candidates containing alias: `)
console.log(sources)

if (candidates.isEmpty) {console.log("Empty Candidates")}
else {
	let fm = sources[0]
	let fileSource = mdc.getFileCache(file)
	if ("frontmatter" in fileSource) {
		fileSource = fileSource.frontmatter
		if ("source" in fileSource) {
			if (fileSource.source != null) {
				fileSource = fileSource.source
				if(Array.isArray(fileSource)) {
					await update("source",JSON.stringify(fileSource.push(fm),null,2).replace(/"([^"]+)":/g, '$1:'),file)
					new Notice (tp.file.title + " - Source Field Updated",4000)
				} else {
					await update("source",JSON.stringify(new Array(fileSource, fm),null,2).replace(/"([^"]+)":/g, '$1:'),file)
					new Notice (tp.file.title + " - Source Field Updated",4000)
				}
			} else {
				await update("source", JSON.stringify(fm,null,2).replace(/"([^"]+)":/g, '$1:'),file)
				new Notice (tp.file.title + " - Source Field Added",4000)
			}
		} else {
			newFileContent = tp.file.content.split("\n")
			newFileCOntent = newFileContent.splice(1,0, `source: ${JSON.stringify(fm)}`)
			console.log(newFileContent)
			await app.vault.modify(file, newFileContent.join("\n"))
			new Notice (tp.file.title + " - Source Field Added",4000)
		}
	} else {
		new Notice (tp.file.title + " - No Frontmatter Found",4000)
	}
}

_%>
