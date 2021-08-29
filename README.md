# blender_curve_export

Will generate a es6 file with all the curves of your Blender scene, already formated for Threejs.


## Usage:

```jsx
import {curveA} from './BlenderFileName.curves'

const points = curveA()
console.log(points) // <-- [THREE.Vector3()]
const path = new CatmullRomCurve3(points)
```

## Template generated:
```jsx
import * as THREE from 'three';

const format = () => {
  for (var i = 0; i < points.length; i++) {
    var x = points[i][0];
    var y = points[i][1];
    var z = points[i][2];
    points[i] = new THREE.Vector3(x, z, -y);
  }
  return points
}

export const curveA = () => {
  const points = [...] <-- exported from blender
	return format(points);
}

export const curveB = () => {
  const points = [...] <-- exported from blender
	return format(points);
}
```

