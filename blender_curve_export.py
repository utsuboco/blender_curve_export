import bpy
import os


currPath = os.path.splitext(bpy.data.filepath)[0]+ ".curves.js"
file = open(currPath, "w") 
file.write('import * as THREE from \'three\';\n')

file.write("const format = (points) => {\n")
file.write("for (var i = 0; i < points.length; i++) {\n")
file.write("  var x = points[i][0];\n")
file.write("  var y = points[i][1];\n")
file.write("  var z = points[i][2];\n")
file.write("  points[i] = new THREE.Vector3(x, z, -y);\n")
file.write("}\n")
file.write("return points;\n")
file.write("}\n")

for ob in bpy.data.objects.values() : 
  if ob.type == 'CURVE' :
    file.write('\n')
    file.write("export const %s = () => {\n const points = [\n" % ob.name.replace('.', ''))
    for spline in ob.data.splines :
      curvetype = spline.type
      print('curve type:', curvetype)

      if curvetype == 'NURBS' or 'POLY':
          if len(spline.points) > 0 :
            for bezier_point in spline.points.values() : 
              co           = ob.matrix_world @ bezier_point.co
              file.write("[%.3f, %.3f, %.3f],  " % (co.x, co.y, co.z ))

      if curvetype == 'BEZIER':
          if len(spline.bezier_points) > 0 :
            for bezier_point in spline.bezier_points.values() : 
              co           = ob.matrix_world @ bezier_point.co
              file.write("[%.3f, %.3f, %.3f],  " % (co.x, co.y, co.z ))
            
    file.write("]\n")
    file.write("return format(points);\n")
    file.write("}\n")
file.write("\n")
file.close()
