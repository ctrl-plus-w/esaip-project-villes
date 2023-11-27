
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');


ctx.fillStyle = "#000000";

const cities = [
{ name: "NorthWest                    ", lat: 52, lng: -5.888519},
{ name: "SouthEst                     ", lat:  40.740, lng: 10.5},
{ name: "Brest                        ", lat: 48.383, lng: -4.500, },
{ name: "Quimper                      ", lat: 48.000, lng: -4.100, },
{ name: "Lorient                      ", lat: 47.750, lng: -3.350, },
{ name: "Saint-Brieuc                 ", lat: 48.517, lng: -2.750, },
{ name: "Vannes                       ", lat: 47.667, lng: -2.733, },
{ name: "Saint-Nazaire                ", lat: 47.283, lng: -2.200, },
{ name: "Rennes                       ", lat: 48.100, lng: -1.667, },
{ name: "Cherbourg                    ", lat: 49.633, lng: -1.617, },
{ name: "Nantes                       ", lat: 47.233, lng: -1.583, },
{ name: "LaRoche-sur-Yon              ", lat: 46.633, lng: -1.500, },
{ name: "Bayonne                      ", lat: 43.500, lng: -1.467, },
{ name: "LaRochelle                   ", lat: 46.167, lng: -1.167, },
{ name: "Saint-Lô                     ", lat: 49.117, lng: -1.083, },
{ name: "Laval                        ", lat: 48.067, lng: -0.750, },
{ name: "Bordeaux                     ", lat: 44.833, lng: -0.567, },
{ name: "Anersg                       ", lat: 47.483, lng: -0.533, },
{ name: "Montde Marsan                ", lat: 43.900, lng: -0.500, },
{ name: "Niort                        ", lat: 46.317, lng: -0.450, },
{ name: "Pau                          ", lat: 43.300, lng: -0.367, },
{ name: "Caen                         ", lat: 49.183, lng: -0.367, },
{ name: "Alençon                      ", lat: 48.417, lng:  0.083, },
{ name: "Tarbes                       ", lat: 43.233, lng:  0.083, },
{ name: "LeHavre                      ", lat: 49.500, lng:  0.100, },
{ name: "Anoulêmeg                    ", lat: 45.667, lng:  0.167, },
{ name: "LeMans                       ", lat: 48.000, lng:  0.200, },
{ name: "Poitiers                     ", lat: 46.583, lng:  0.333, },
{ name: "Cahors                       ", lat: 44.467, lng:  0.433, },
{ name: "Auch                         ", lat: 43.650, lng:  0.583, },
{ name: "Aeng                         ", lat: 44.200, lng:  0.617, },
{ name: "Tours                        ", lat: 47.383, lng:  0.700, },
{ name: "Périueuxg                    ", lat: 45.183, lng:  0.717, },
{ name: "Dieppe                       ", lat: 49.917, lng:  1.083, },
{ name: "Rouen                        ", lat: 49.433, lng:  1.083, },
{ name: "Evreux                       ", lat: 49.050, lng:  1.183, },
{ name: "Limoesg                      ", lat: 45.833, lng:  1.250, },
{ name: "Montauban                    ", lat: 44.017, lng:  1.333, },
{ name: "Blois                        ", lat: 47.600, lng:  1.333, },
{ name: "Toulouse                     ", lat: 43.617, lng:  1.450, },
{ name: "Chartres                     ", lat: 48.450, lng:  1.500, },
{ name: "Foix                         ", lat: 42.950, lng:  1.583, },
{ name: "Châteauroux                  ", lat: 46.817, lng:  1.683, },
{ name: "Tulle                        ", lat: 45.267, lng:  1.767, },
{ name: "Abbeville                    ", lat: 50.100, lng:  1.850, },
{ name: "Guéret                       ", lat: 46.167, lng:  1.866, },
{ name: "Orléans                      ", lat: 47.900, lng:  1.900, },
{ name: "Vierzon                      ", lat: 47.233, lng:  2.050, },
{ name: "Pontoise                     ", lat: 49.050, lng:  2.083, },
{ name: "Beauvais                     ", lat: 49.433, lng:  2.083, },
{ name: "Versailles                   ", lat: 48.800, lng:  2.133, },
{ name: "Albi                         ", lat: 43.933, lng:  2.144, },
{ name: "Nanterre                     ", lat: 48.883, lng:  2.217, },
{ name: "Amiens                       ", lat: 49.900, lng:  2.300, },
{ name: "Paris                        ", lat: 48.833, lng:  2.333, },
{ name: "Bouresg                      ", lat: 47.083, lng:  2.383, },
{ name: "Carcassonne                  ", lat: 43.217, lng:  2.350, },
{ name: "Dunkerque                    ", lat: 51.033, lng:  2.383, },
{ name: "Aurillac                     ", lat: 44.933, lng:  2.433, },
{ name: "Bobinyg                      ", lat: 48.917, lng:  2.450, },
{ name: "Créteil                      ", lat: 48.783, lng:  2.467, },
{ name: "Melun                        ", lat: 48.533, lng:  2.557, },
{ name: "Evry                         ", lat: 48.633, lng:  2.567, },
{ name: "Rodez                        ", lat: 44.350, lng:  2.567, },
{ name: "Montluçon                    ", lat: 46.333, lng:  2.600, },
{ name: "Arras                        ", lat: 50.283, lng:  2.767, },
{ name: "Lens                         ", lat: 50.433, lng:  2.833, },
{ name: "Perpinang                    ", lat: 42.700, lng:  2.900, },
{ name: "Lille                        ", lat: 50.650, lng:  3.083, },
{ name: "Clermont-Ferrand             ", lat: 45.783, lng:  3.083, },
{ name: "Nevers                       ", lat: 47.000, lng:  3.150, },
{ name: "Moulins                      ", lat: 46.567, lng:  3.333, },
{ name: "Mende                        ", lat: 44.533, lng:  3.500, },
{ name: "Auxerre                      ", lat: 47.800, lng:  3.583, },
{ name: "Laon                         ", lat: 49.567, lng:  3.617, },
{ name: "Montpellier                  ", lat: 43.600, lng:  3.883, },
{ name: "LePuy                        ", lat: 45.050, lng:  3.883, },
{ name: "Avallon                      ", lat: 47.500, lng:  3.900, },
{ name: "Reims                        ", lat: 49.250, lng:  4.033, },
{ name: "Troyes                       ", lat: 48.300, lng:  4.083, },
{ name: "Roanne                       ", lat: 46.033, lng:  4.067, },
{ name: "Nîmes                        ", lat: 43.833, lng:  4.366, },
{ name: "Chalonssur Marne             ", lat: 48.967, lng:  4.367, },
{ name: "Saint-Etienne                ", lat: 45.433, lng:  4.383, },
{ name: "Privas                       ", lat: 44.733, lng:  4.600, },
{ name: "Mézières                     ", lat: 49.767, lng:  4.717, },
{ name: "Avinong                      ", lat: 43.933, lng:  4.800, },
{ name: "Lyon                         ", lat: 45.767, lng:  4.833, },
{ name: "Macon                        ", lat: 45.300, lng:  4.833, },
{ name: "Valence                      ", lat: 44.933, lng:  4.900, },
{ name: "Dijon                        ", lat: 47.333, lng:  5.033, },
{ name: "Chaumont                     ", lat: 48.117, lng:  5.133, },
{ name: "Bar-le-Duc                   ", lat: 48.767, lng:  5.167, },
{ name: "Bourg                        ", lat: 46.200, lng:  5.217, },
{ name: "Marseille                    ", lat: 43.300, lng:  5.367, },
{ name: "Lons-le-Saunier              ", lat: 46.683, lng:  5.550, },
{ name: "Grenoble                     ", lat: 45.183, lng:  5.717, },
{ name: "Toulon                       ", lat: 43.117, lng:  5.917, },
{ name: "Chambéry                     ", lat: 45.567, lng:  5.917, },
{ name: "Besançon                     ", lat: 47.250, lng:  6.017, },
{ name: "Gap                          ", lat: 44.550, lng:  6.083, },
{ name: "Annecy                       ", lat: 45.900, lng:  6.117, },
{ name: "Metz                         ", lat: 49.117, lng:  6.183, },
{ name: "Vesoul                       ", lat: 47.633, lng:  6.150, },
{ name: "Nancy                        ", lat: 48.700, lng:  6.200, },
{ name: "Dineg                        ", lat: 44.083, lng:  6.233, },
{ name: "Epinal                       ", lat: 48.167, lng:  6.467, },
{ name: "Belfort                      ", lat: 47.633, lng:  6.867, },
{ name: "Cannes                       ", lat: 43.550, lng:  7.000, },
{ name: "Nice                         ", lat: 43.700, lng:  7.267, },
{ name: "Colmar                       ", lat: 48.083, lng:  7.350, },
{ name: "Mulhouse                     ", lat: 47.750, lng:  7.350, },
{ name: "Strasbourg                   ", lat: 48.583, lng:  7.750, },
{ name: "Ajaccio                      ", lat: 41.917, lng:  8.717, },
{ name: "Bastia                       ", lat: 42.683, lng:  9.433, },
].map(({lat,lng, ...obj}) => ({ lng: lat, lat: lng, ...obj}));

const scale = (number, [inMin, inMax], [outMin, outMax]) => {
  return (number - inMin) / (inMax - inMin) * (outMax - outMin) + outMin;
}

const lats = cities.map(({ lat }) => lat);
const lngs = cities.map(({ lng }) => lng);

const minLat = Math.min(...lats);
const maxLat = Math.max(...lats);
const minLng = Math.min(...lngs);
const maxLng = Math.max(...lngs);

const mCities = cities.map((city) => ({
  x: scale(city.lat, [minLat, maxLat], [0, 516]),
  y: scale(city.lng, [minLng, maxLng], [0, 494]),
  ...city,
}))

const xs = mCities.map(({ x }) => x);
const ys = mCities.map(({ y }) => y);

const minX = Math.min(...xs);
const maxX = Math.max(...xs);
const minY = Math.min(...ys);
const maxY = Math.max(...ys);


const offsetYLeft = mCities.find(({ lng }) => lng === minLng).y;
const offsetYRight = mCities.find(({ lng }) => lng === maxLng).y;

for (const city of mCities) {
  const { x, y } = city;

  // const _x = scale(x, [0, 516], [516, 0]);
  const _y = scale(y, [0, 494], [494, 0]);
  // const _y = y;
  const _x = x;

  ctx.fillRect(_x - 2,_y - 2, 4, 4);
}
