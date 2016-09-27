import sys, os

from gradebook.score import (
    init_parts,
    check,
    DEVNULL,
    R,
    run,
    query,
)

R('options(device=pdf)')  # put graphics in a file
r_source = R['source']
work_dir = os.getcwd()

part_names = ['ex1', 'ex2', 'ex3', 'ex4']
possible = [6, 8, 8, 8]

g = globals()

# Score part 0
def ex1(assignment, score=0):
    part = part_names[0]
    try:
        m = r_source("/".join([work_dir, assignment, part])+'.r', chdir=True)
        #exec("""R('source("'+part+'.r")')""", g)
    except:
        pass

    R('graphics.off()')  # tell R to finalize plots

    run("R('load(\\'../instructor/hw1/ex1-tests2.rda\\')')", g)
    score += check("R('all.equal(outlier.cutoff.t, outlierCutoff(ex1.test))')[0]", True, 2, g)
    score += check("R('all.equal(remove.outlier.t, removeOutliers(ex1.test, 0.25))')[0]", True, 2, g)
    score += check("R('all.equal(remove.outlier.t.2, removeOutliers(ex1.test, 0.10))')[0]", True, 2, g)

    return score

# Score part 1
def ex2(assignment, score=0):
    part = part_names[1]
    try:
        m = r_source("/".join([work_dir, assignment, part])+'.r', chdir = True)
        #exec("""R('source("'+part+'.r")')""", g)
    except:
        pass

    R('graphics.off()')  # tell R to finalize plots

    run("R('load(\\'hw1/ex2-tests.rda\\')')", g)
    run("R('set.seed(47)')", g)
    run("R('x = simpleNormSim(c(25, 50, 75))')", g)
    score += check("R('is.list(x)')[0]", True, 2, g)
    score += check("R('all.equal(simple.norm.sim.t, x)')[0]", True, 2, g)
    run("R('sizes_t = c(25, 50, 25, 50)')", g)
    run("R('means_t = c(0, 5, 5, 0)')", g)
    run("R('vars_t = c(1, 2, 1, 2)')", g)
    run("R('set.seed(47)')", g)
    run("R('x = advancedNormSim(sizes_t, means_t, vars_t)')", g)
    score += check("R('is.list(x)')[0]", True, 2, g)
    score += check("R('all.equal(advanced.norm.sim.t, x)')[0]", True, 2, g)

    return score

# Score part 2
def ex3(assignment, score=0):
    part = part_names[2]
    try:
        m = r_source("/".join([work_dir, assignment, part])+'.r', chdir = True)
        #exec("""R('source("'+part+'.r")')""", g)
    except:
        pass

    R('graphics.off()')  # tell R to finalize plots

    run("R('load(\\'hw1/ex3-tests.rda\\')')", g)
    run("R('set.seed(47)')", g)
    run("R('x =  meanByLevel(iris)')", g)
    score += check("R('is.matrix(x)')[0]", True, 2, g)
    score += check("R('all.equal(mean.by.level.t, x)')[0]", True, 2, g)
    run("R('x = stdLevelDiff(iris)')", g)
    score += check("R('is.matrix(x)')[0]", True, 2, g)
    score += check("R('all.equal(std.level.diff.t, abs(x))')[0]", True, 2, g)

    return score

# Score part 3
def ex4(assignment, score=0):
    part = part_names[3]
    try:
        m = r_source("/".join([work_dir, assignment, part])+'.r', chdir = True)
        #exec("""R('source("'+part+'.r")')""", g)
    except:
        pass

    R('graphics.off()')  # tell R to finalize plots

    run("R('load(\\'hw1/ex4-tests.rda\\')')", g)
    score += check("R('all.equal(numeric(0), identifyDuplicates(ex4.test1))')[0]", True, 2, g)
    run("R('x = identifyDuplicates(ex4.test2)')", g)
    score += check("R('is.matrix(x)')[0]", True, 2, g)
    score += check("R('if (is.null(x)) FALSE else is.null(names(x))')[0]", True, 2, g)
    score += check("R('all.equal(identify.duplicates.t, x)')[0]", True, 2, g)

    return score

