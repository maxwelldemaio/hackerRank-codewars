/*
You will be given an array of object, every object might be composed like that:

{
  type: 'box',
  material: 'paper'
}
or like that:

{
  type: 'bottle',
  material: 'glass',
  secondMaterial: 'paper'
}
Those are the materials that you might encounter: paper, glass, organic, plastic.

An object can be made by one or two materials.

If an object is made of two materials recycle it on BOTH of the correct bins.

Recycle all the objects in a new nested array where the first nested array will contain paper, 
the second glass, the third organic and the fourth plastic, so given this array of objects:

[
{
  type: 'rotten apples',
  material: 'organic'
},
{
  type: 'out of date yogurt',
  material: 'organic',
  secondMaterial: 'plastic'
},
{
  type: 'wine bottle',
  material: 'glass',
  secondMaterial: 'paper'
},
{
  type: 'amazon box',
  material: 'paper'
},
{
  type: 'beer bottle',
  material: 'glass',
  secondMaterial: 'paper'
}
]
You should return this nested array:

[['wine bottle', 'amazon box', 'beer bottle'], ['wine bottle', 'beer bottle'], ['rotten apples', 'out of date yogurt'], ['out of date yogurt']]
Rules:

-There will always be the type and material property on every object, in some object there will be the secondMaterial property.

-All the input provided will always have one or more valid object.

-Always return a nested array with all the four bins inside even if they are empty, 
example: [['wine bottle', 'amazon box', 'beer bottle'], [], ['rotten apples', 'out of date yogurt'], []]

-Put the items in the bins in the same order that you find it.

P.S Don't freak out if you encounter an organic bottle or a plastic apple, we are making some biotech experiments...
*/

function recycle(array) {
    // Create bins for recycling
    paper = []
    glass = []
    organic = []
    plastic = []

    // Loop over items to be recycled
    for (var x = 0; x < array.length; x++) {
      // Sort based on first material
      switch (array[x].material) {
        case "paper":
          paper.push(array[x].type);
          break;
        case "glass":
          glass.push(array[x].type);
          break;
        case "organic":
          organic.push(array[x].type);
          break;
        case "plastic":
          plastic.push(array[x].type);
      }
        // If there is a second material, sort based on second material
      if (array[x].secondMaterial) {
        switch (array[x].secondMaterial) {
          case "paper":
            paper.push(array[x].type);
            break;
          case "glass":
            glass.push(array[x].type);
            break;
          case "organic":
            organic.push(array[x].type);
            break;
          case "plastic":
            plastic.push(array[x].type);
        }
      }
    }
  
    // Put bins in one large bin to be recycled
    return [paper, glass, organic, plastic];
}


// Test Case 1
console.log(recycle(
    [
        {
            type: 'rotten apples',
            material: 'organic'
        },
        {
            type: 'out of date yogurt',
            material: 'organic',
            secondMaterial: 'plastic'
        },
        {
            type: 'wine bottle',
            material: 'glass',
            secondMaterial: 'paper'
        },
        {
            type: 'amazon box',
            material: 'paper'
        },
        {
            type: 'beer bottle',
            material: 'glass',
            secondMaterial: 'paper'
        }
    ]
));