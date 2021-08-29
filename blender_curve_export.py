import bpy
import os


currPath = os.path.splitext(bpy.data.filepath)[0]+ ".curves.js"
file = open(currPath, "w") 

file.write('const curve = {\n')
for ob in bpy.data.objects.values() : 
  if ob.type == 'CURVE' :
    file.write( '"%s":\n' % ob.name)
    for spline in ob.data.splines :
      curvetype = spline.type
      print('curve type:', curvetype)

      if curvetype == 'NURBS' or 'POLY':
          if len(spline.points) > 0 :
            file.write("[")
            for bezier_point in spline.points.values() : 
              co           = bezier_point.co @ ob.matrix_world
              file.write("[%.3f, %.3f, %.3f],  " % (co.x, co.y, co.z ))

      if curvetype == 'BEZIER':
          if len(spline.bezier_points) > 0 :
            file.write("[")
            for bezier_point in spline.bezier_points.values() : 
              co           = bezier_point.co @ ob.matrix_world
              file.write("[%.3f, %.3f, %.3f],  " % (co.x, co.y, co.z ))
            

    file.write("],\n")
file.write("}\n")
file.write("\n")
file.write("export default curve")
file.write("\n")
file.close()
