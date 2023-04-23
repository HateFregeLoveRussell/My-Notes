<%*
type = await tp.system.suggester(["HW", "Assignment", "Project", "Lab"],["HW", "Assignment", "Project", "Lab"],false)
tR += `{type: ${type}, `
if (type != "HW") {
	decision = await tp.system.suggester(["standard", "non-standard"],["standard", "non-standard"],false)
	tR += `grading: ${decision}, `
	if (decision === "standard") {
		tR += `weight: ` _%>
	<%_tp.file.cursor()_%>
<%_*
	}
	if (decision === "standard") {
		tR += `, `
	}
} 
tR += `due: `
_%>
<%_tp.file.cursor()%>, alias: <%tp.file.cursor() _%>,  
<%_* tR += ` template: {name: deliverable-obj, version: 1}}` _%>


