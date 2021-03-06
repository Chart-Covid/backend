import json
from django.http import HttpResponse

def all_countries(requests):
    data = [{'name': 'Afghanistan',
        'flag': 'https://disease.sh/assets/img/flags/af.png',
        'location': {'lat': 33, 'lng': 65}},
        {'name': 'Albania',
        'flag': 'https://disease.sh/assets/img/flags/al.png',
        'location': {'lat': 41, 'lng': 20}},
        {'name': 'Algeria',
        'flag': 'https://disease.sh/assets/img/flags/dz.png',
        'location': {'lat': 28, 'lng': 3}},
        {'name': 'Andorra',
        'flag': 'https://disease.sh/assets/img/flags/ad.png',
        'location': {'lat': 42.5, 'lng': 1.6}},
        {'name': 'Angola',
        'flag': 'https://disease.sh/assets/img/flags/ao.png',
        'location': {'lat': -12.5, 'lng': 18.5}},
        {'name': 'Anguilla',
        'flag': 'https://disease.sh/assets/img/flags/ai.png',
        'location': {'lat': 18.25, 'lng': -63.1667}},
        {'name': 'Antigua and Barbuda',
        'flag': 'https://disease.sh/assets/img/flags/ag.png',
        'location': {'lat': 17.05, 'lng': -61.8}},
        {'name': 'Argentina',
        'flag': 'https://disease.sh/assets/img/flags/ar.png',
        'location': {'lat': -34, 'lng': -64}},
        {'name': 'Armenia',
        'flag': 'https://disease.sh/assets/img/flags/am.png',
        'location': {'lat': 40, 'lng': 45}},
        {'name': 'Aruba',
        'flag': 'https://disease.sh/assets/img/flags/aw.png',
        'location': {'lat': 12.5, 'lng': -69.9667}},
        {'name': 'Australia',
        'flag': 'https://disease.sh/assets/img/flags/au.png',
        'location': {'lat': -27, 'lng': 133}},
        {'name': 'Austria',
        'flag': 'https://disease.sh/assets/img/flags/at.png',
        'location': {'lat': 47.3333, 'lng': 13.3333}},
        {'name': 'Azerbaijan',
        'flag': 'https://disease.sh/assets/img/flags/az.png',
        'location': {'lat': 40.5, 'lng': 47.5}},
        {'name': 'Bahamas',
        'flag': 'https://disease.sh/assets/img/flags/bs.png',
        'location': {'lat': 24.25, 'lng': -76}},
        {'name': 'Bahrain',
        'flag': 'https://disease.sh/assets/img/flags/bh.png',
        'location': {'lat': 26, 'lng': 50.55}},
        {'name': 'Bangladesh',
        'flag': 'https://disease.sh/assets/img/flags/bd.png',
        'location': {'lat': 24, 'lng': 90}},
        {'name': 'Barbados',
        'flag': 'https://disease.sh/assets/img/flags/bb.png',
        'location': {'lat': 13.1667, 'lng': -59.5333}},
        {'name': 'Belarus',
        'flag': 'https://disease.sh/assets/img/flags/by.png',
        'location': {'lat': 53, 'lng': 28}},
        {'name': 'Belgium',
        'flag': 'https://disease.sh/assets/img/flags/be.png',
        'location': {'lat': 50.8333, 'lng': 4}},
        {'name': 'Belize',
        'flag': 'https://disease.sh/assets/img/flags/bz.png',
        'location': {'lat': 17.25, 'lng': -88.75}},
        {'name': 'Benin',
        'flag': 'https://disease.sh/assets/img/flags/bj.png',
        'location': {'lat': 9.5, 'lng': 2.25}},
        {'name': 'Bermuda',
        'flag': 'https://disease.sh/assets/img/flags/bm.png',
        'location': {'lat': 32.3333, 'lng': -64.75}},
        {'name': 'Bhutan',
        'flag': 'https://disease.sh/assets/img/flags/bt.png',
        'location': {'lat': 27.5, 'lng': 90.5}},
        {'name': 'Bolivia',
        'flag': 'https://disease.sh/assets/img/flags/bo.png',
        'location': {'lat': -17, 'lng': -65}},
        {'name': 'Bosnia',
        'flag': 'https://disease.sh/assets/img/flags/ba.png',
        'location': {'lat': 44, 'lng': 18}},
        {'name': 'Botswana',
        'flag': 'https://disease.sh/assets/img/flags/bw.png',
        'location': {'lat': -22, 'lng': 24}},
        {'name': 'Brazil',
        'flag': 'https://disease.sh/assets/img/flags/br.png',
        'location': {'lat': -10, 'lng': -55}},
        {'name': 'British Virgin Islands',
        'flag': 'https://disease.sh/assets/img/flags/vg.png',
        'location': {'lat': 18.5, 'lng': -64.5}},
        {'name': 'Brunei',
        'flag': 'https://disease.sh/assets/img/flags/bn.png',
        'location': {'lat': 4.5, 'lng': 114.6667}},
        {'name': 'Bulgaria',
        'flag': 'https://disease.sh/assets/img/flags/bg.png',
        'location': {'lat': 43, 'lng': 25}},
        {'name': 'Burkina Faso',
        'flag': 'https://disease.sh/assets/img/flags/bf.png',
        'location': {'lat': 13, 'lng': -2}},
        {'name': 'Burundi',
        'flag': 'https://disease.sh/assets/img/flags/bi.png',
        'location': {'lat': -3.5, 'lng': 30}},
        {'name': 'Cabo Verde',
        'flag': 'https://disease.sh/assets/img/flags/cv.png',
        'location': {'lat': 16, 'lng': -24}},
        {'name': 'Cambodia',
        'flag': 'https://disease.sh/assets/img/flags/kh.png',
        'location': {'lat': 13, 'lng': 105}},
        {'name': 'Cameroon',
        'flag': 'https://disease.sh/assets/img/flags/cm.png',
        'location': {'lat': 6, 'lng': 12}},
        {'name': 'Canada',
        'flag': 'https://disease.sh/assets/img/flags/ca.png',
        'location': {'lat': 60, 'lng': -95}},
        {'name': 'Caribbean Netherlands',
        'flag': 'https://disease.sh/assets/img/flags/bq.png',
        'location': {'lat': 12.2, 'lng': -68.26}},
        {'name': 'Cayman Islands',
        'flag': 'https://disease.sh/assets/img/flags/ky.png',
        'location': {'lat': 19.5, 'lng': -80.5}},
        {'name': 'Central African Republic',
        'flag': 'https://disease.sh/assets/img/flags/cf.png',
        'location': {'lat': 7, 'lng': 21}},
        {'name': 'Chad',
        'flag': 'https://disease.sh/assets/img/flags/td.png',
        'location': {'lat': 15, 'lng': 19}},
        {'name': 'Channel Islands',
        'flag': 'https://disease.sh/assets/img/flags/je.png',
        'location': {'lat': 49.21, 'lng': -2.13}},
        {'name': 'Chile',
        'flag': 'https://disease.sh/assets/img/flags/cl.png',
        'location': {'lat': -30, 'lng': -71}},
        {'name': 'China',
        'flag': 'https://disease.sh/assets/img/flags/cn.png',
        'location': {'lat': 35, 'lng': 105}},
        {'name': 'Colombia',
        'flag': 'https://disease.sh/assets/img/flags/co.png',
        'location': {'lat': 4, 'lng': -72}},
        {'name': 'Comoros',
        'flag': 'https://disease.sh/assets/img/flags/km.png',
        'location': {'lat': -12.1667, 'lng': 44.25}},
        {'name': 'Congo',
        'flag': 'https://disease.sh/assets/img/flags/cg.png',
        'location': {'lat': -1, 'lng': 15}},
        {'name': 'Costa Rica',
        'flag': 'https://disease.sh/assets/img/flags/cr.png',
        'location': {'lat': 10, 'lng': -84}},
        {'name': 'Croatia',
        'flag': 'https://disease.sh/assets/img/flags/hr.png',
        'location': {'lat': 45.1667, 'lng': 15.5}},
        {'name': 'Cuba',
        'flag': 'https://disease.sh/assets/img/flags/cu.png',
        'location': {'lat': 21.5, 'lng': -80}},
        {'name': 'Curaçao',
        'flag': 'https://disease.sh/assets/img/flags/cw.png',
        'location': {'lat': 12.15, 'lng': -68.97}},
        {'name': 'Cyprus',
        'flag': 'https://disease.sh/assets/img/flags/cy.png',
        'location': {'lat': 35, 'lng': 33}},
        {'name': 'Czechia',
        'flag': 'https://disease.sh/assets/img/flags/cz.png',
        'location': {'lat': 49.75, 'lng': 15.5}},
        {'name': "Côte d'Ivoire",
        'flag': 'https://disease.sh/assets/img/flags/ci.png',
        'location': {'lat': 8, 'lng': -5}},
        {'name': 'DRC',
        'flag': 'https://disease.sh/assets/img/flags/cd.png',
        'location': {'lat': 0, 'lng': 25}},
        {'name': 'Denmark',
        'flag': 'https://disease.sh/assets/img/flags/dk.png',
        'location': {'lat': 56, 'lng': 10}},
        {'name': 'Diamond Princess',
        'flag': 'https://disease.sh/assets/img/flags/unknown.png',
        'location': {'lat': 0, 'lng': 0}},
        {'name': 'Djibouti',
        'flag': 'https://disease.sh/assets/img/flags/dj.png',
        'location': {'lat': 11.5, 'lng': 43}},
        {'name': 'Dominica',
        'flag': 'https://disease.sh/assets/img/flags/dm.png',
        'location': {'lat': 15.4167, 'lng': -61.3333}},
        {'name': 'Dominican Republic',
        'flag': 'https://disease.sh/assets/img/flags/do.png',
        'location': {'lat': 19, 'lng': -70.6667}},
        {'name': 'Ecuador',
        'flag': 'https://disease.sh/assets/img/flags/ec.png',
        'location': {'lat': -2, 'lng': -77.5}},
        {'name': 'Egypt',
        'flag': 'https://disease.sh/assets/img/flags/eg.png',
        'location': {'lat': 27, 'lng': 30}},
        {'name': 'El Salvador',
        'flag': 'https://disease.sh/assets/img/flags/sv.png',
        'location': {'lat': 13.8333, 'lng': -88.9167}},
        {'name': 'Equatorial Guinea',
        'flag': 'https://disease.sh/assets/img/flags/gq.png',
        'location': {'lat': 2, 'lng': 10}},
        {'name': 'Eritrea',
        'flag': 'https://disease.sh/assets/img/flags/er.png',
        'location': {'lat': 15, 'lng': 39}},
        {'name': 'Estonia',
        'flag': 'https://disease.sh/assets/img/flags/ee.png',
        'location': {'lat': 59, 'lng': 26}},
        {'name': 'Ethiopia',
        'flag': 'https://disease.sh/assets/img/flags/et.png',
        'location': {'lat': 8, 'lng': 38}},
        {'name': 'Falkland Islands (Malvinas)',
        'flag': 'https://disease.sh/assets/img/flags/fk.png',
        'location': {'lat': -51.75, 'lng': -59}},
        {'name': 'Faroe Islands',
        'flag': 'https://disease.sh/assets/img/flags/fo.png',
        'location': {'lat': 62, 'lng': -7}},
        {'name': 'Fiji',
        'flag': 'https://disease.sh/assets/img/flags/fj.png',
        'location': {'lat': -18, 'lng': 175}},
        {'name': 'Finland',
        'flag': 'https://disease.sh/assets/img/flags/fi.png',
        'location': {'lat': 64, 'lng': 26}},
        {'name': 'France',
        'flag': 'https://disease.sh/assets/img/flags/fr.png',
        'location': {'lat': 46, 'lng': 2}},
        {'name': 'French Guiana',
        'flag': 'https://disease.sh/assets/img/flags/gf.png',
        'location': {'lat': 4, 'lng': -53}},
        {'name': 'French Polynesia',
        'flag': 'https://disease.sh/assets/img/flags/pf.png',
        'location': {'lat': -15, 'lng': -140}},
        {'name': 'Gabon',
        'flag': 'https://disease.sh/assets/img/flags/ga.png',
        'location': {'lat': -1, 'lng': 11.75}},
        {'name': 'Gambia',
        'flag': 'https://disease.sh/assets/img/flags/gm.png',
        'location': {'lat': 13.4667, 'lng': -16.5667}},
        {'name': 'Georgia',
        'flag': 'https://disease.sh/assets/img/flags/ge.png',
        'location': {'lat': 42, 'lng': 43.5}},
        {'name': 'Germany',
        'flag': 'https://disease.sh/assets/img/flags/de.png',
        'location': {'lat': 51, 'lng': 9}},
        {'name': 'Ghana',
        'flag': 'https://disease.sh/assets/img/flags/gh.png',
        'location': {'lat': 8, 'lng': -2}},
        {'name': 'Gibraltar',
        'flag': 'https://disease.sh/assets/img/flags/gi.png',
        'location': {'lat': 36.1833, 'lng': -5.3667}},
        {'name': 'Greece',
        'flag': 'https://disease.sh/assets/img/flags/gr.png',
        'location': {'lat': 39, 'lng': 22}},
        {'name': 'Greenland',
        'flag': 'https://disease.sh/assets/img/flags/gl.png',
        'location': {'lat': 72, 'lng': -40}},
        {'name': 'Grenada',
        'flag': 'https://disease.sh/assets/img/flags/gd.png',
        'location': {'lat': 12.1167, 'lng': -61.6667}},
        {'name': 'Guadeloupe',
        'flag': 'https://disease.sh/assets/img/flags/gp.png',
        'location': {'lat': 16.25, 'lng': -61.5833}},
        {'name': 'Guatemala',
        'flag': 'https://disease.sh/assets/img/flags/gt.png',
        'location': {'lat': 15.5, 'lng': -90.25}},
        {'name': 'Guinea',
        'flag': 'https://disease.sh/assets/img/flags/gn.png',
        'location': {'lat': 11, 'lng': -10}},
        {'name': 'Guinea-Bissau',
        'flag': 'https://disease.sh/assets/img/flags/gw.png',
        'location': {'lat': 12, 'lng': -15}},
        {'name': 'Guyana',
        'flag': 'https://disease.sh/assets/img/flags/gy.png',
        'location': {'lat': 5, 'lng': -59}},
        {'name': 'Haiti',
        'flag': 'https://disease.sh/assets/img/flags/ht.png',
        'location': {'lat': 19, 'lng': -72.4167}},
        {'name': 'Holy See (Vatican City State)',
        'flag': 'https://disease.sh/assets/img/flags/va.png',
        'location': {'lat': 41.9, 'lng': 12.45}},
        {'name': 'Honduras',
        'flag': 'https://disease.sh/assets/img/flags/hn.png',
        'location': {'lat': 15, 'lng': -86.5}},
        {'name': 'Hong Kong',
        'flag': 'https://disease.sh/assets/img/flags/hk.png',
        'location': {'lat': 22.25, 'lng': 114.1667}},
        {'name': 'Hungary',
        'flag': 'https://disease.sh/assets/img/flags/hu.png',
        'location': {'lat': 47, 'lng': 20}},
        {'name': 'Iceland',
        'flag': 'https://disease.sh/assets/img/flags/is.png',
        'location': {'lat': 65, 'lng': -18}},
        {'name': 'India',
        'flag': 'https://disease.sh/assets/img/flags/in.png',
        'location': {'lat': 20, 'lng': 77}},
        {'name': 'Indonesia',
        'flag': 'https://disease.sh/assets/img/flags/id.png',
        'location': {'lat': -5, 'lng': 120}},
        {'name': 'Iran',
        'flag': 'https://disease.sh/assets/img/flags/ir.png',
        'location': {'lat': 32, 'lng': 53}},
        {'name': 'Iraq',
        'flag': 'https://disease.sh/assets/img/flags/iq.png',
        'location': {'lat': 33, 'lng': 44}},
        {'name': 'Ireland',
        'flag': 'https://disease.sh/assets/img/flags/ie.png',
        'location': {'lat': 53, 'lng': -8}},
        {'name': 'Isle of Man',
        'flag': 'https://disease.sh/assets/img/flags/im.png',
        'location': {'lat': 54.23, 'lng': -4.55}},
        {'name': 'Israel',
        'flag': 'https://disease.sh/assets/img/flags/il.png',
        'location': {'lat': 31.5, 'lng': 34.75}},
        {'name': 'Italy',
        'flag': 'https://disease.sh/assets/img/flags/it.png',
        'location': {'lat': 42.8333, 'lng': 12.8333}},
        {'name': 'Jamaica',
        'flag': 'https://disease.sh/assets/img/flags/jm.png',
        'location': {'lat': 18.25, 'lng': -77.5}},
        {'name': 'Japan',
        'flag': 'https://disease.sh/assets/img/flags/jp.png',
        'location': {'lat': 36, 'lng': 138}},
        {'name': 'Jordan',
        'flag': 'https://disease.sh/assets/img/flags/jo.png',
        'location': {'lat': 31, 'lng': 36}},
        {'name': 'Kazakhstan',
        'flag': 'https://disease.sh/assets/img/flags/kz.png',
        'location': {'lat': 48, 'lng': 68}},
        {'name': 'Kenya',
        'flag': 'https://disease.sh/assets/img/flags/ke.png',
        'location': {'lat': 1, 'lng': 38}},
        {'name': 'Kuwait',
        'flag': 'https://disease.sh/assets/img/flags/kw.png',
        'location': {'lat': 29.3375, 'lng': 47.6581}},
        {'name': 'Kyrgyzstan',
        'flag': 'https://disease.sh/assets/img/flags/kg.png',
        'location': {'lat': 41, 'lng': 75}},
        {'name': "Lao People's Democratic Republic",
        'flag': 'https://disease.sh/assets/img/flags/la.png',
        'location': {'lat': 18, 'lng': 105}},
        {'name': 'Latvia',
        'flag': 'https://disease.sh/assets/img/flags/lv.png',
        'location': {'lat': 57, 'lng': 25}},
        {'name': 'Lebanon',
        'flag': 'https://disease.sh/assets/img/flags/lb.png',
        'location': {'lat': 33.8333, 'lng': 35.8333}},
        {'name': 'Lesotho',
        'flag': 'https://disease.sh/assets/img/flags/ls.png',
        'location': {'lat': -29.5, 'lng': 28.5}},
        {'name': 'Liberia',
        'flag': 'https://disease.sh/assets/img/flags/lr.png',
        'location': {'lat': 6.5, 'lng': -9.5}},
        {'name': 'Libyan Arab Jamahiriya',
        'flag': 'https://disease.sh/assets/img/flags/ly.png',
        'location': {'lat': 25, 'lng': 17}},
        {'name': 'Liechtenstein',
        'flag': 'https://disease.sh/assets/img/flags/li.png',
        'location': {'lat': 47.1667, 'lng': 9.5333}},
        {'name': 'Lithuania',
        'flag': 'https://disease.sh/assets/img/flags/lt.png',
        'location': {'lat': 56, 'lng': 24}},
        {'name': 'Luxembourg',
        'flag': 'https://disease.sh/assets/img/flags/lu.png',
        'location': {'lat': 49.75, 'lng': 6.1667}},
        {'name': 'MS Zaandam',
        'flag': 'https://disease.sh/assets/img/flags/unknown.png',
        'location': {'lat': 0, 'lng': 0}},
        {'name': 'Macao',
        'flag': 'https://disease.sh/assets/img/flags/mo.png',
        'location': {'lat': 22.1667, 'lng': 113.55}},
        {'name': 'Macedonia',
        'flag': 'https://disease.sh/assets/img/flags/mk.png',
        'location': {'lat': 41.8333, 'lng': 22}},
        {'name': 'Madagascar',
        'flag': 'https://disease.sh/assets/img/flags/mg.png',
        'location': {'lat': -20, 'lng': 47}},
        {'name': 'Malawi',
        'flag': 'https://disease.sh/assets/img/flags/mw.png',
        'location': {'lat': -13.5, 'lng': 34}},
        {'name': 'Malaysia',
        'flag': 'https://disease.sh/assets/img/flags/my.png',
        'location': {'lat': 2.5, 'lng': 112.5}},
        {'name': 'Maldives',
        'flag': 'https://disease.sh/assets/img/flags/mv.png',
        'location': {'lat': 3.25, 'lng': 73}},
        {'name': 'Mali',
        'flag': 'https://disease.sh/assets/img/flags/ml.png',
        'location': {'lat': 17, 'lng': -4}},
        {'name': 'Malta',
        'flag': 'https://disease.sh/assets/img/flags/mt.png',
        'location': {'lat': 35.8333, 'lng': 14.5833}},
        {'name': 'Martinique',
        'flag': 'https://disease.sh/assets/img/flags/mq.png',
        'location': {'lat': 14.6667, 'lng': -61}},
        {'name': 'Mauritania',
        'flag': 'https://disease.sh/assets/img/flags/mr.png',
        'location': {'lat': 20, 'lng': -12}},
        {'name': 'Mauritius',
        'flag': 'https://disease.sh/assets/img/flags/mu.png',
        'location': {'lat': -20.2833, 'lng': 57.55}},
        {'name': 'Mayotte',
        'flag': 'https://disease.sh/assets/img/flags/yt.png',
        'location': {'lat': -12.8333, 'lng': 45.1667}},
        {'name': 'Mexico',
        'flag': 'https://disease.sh/assets/img/flags/mx.png',
        'location': {'lat': 23, 'lng': -102}},
        {'name': 'Moldova',
        'flag': 'https://disease.sh/assets/img/flags/md.png',
        'location': {'lat': 47, 'lng': 29}},
        {'name': 'Monaco',
        'flag': 'https://disease.sh/assets/img/flags/mc.png',
        'location': {'lat': 43.7333, 'lng': 7.4}},
        {'name': 'Mongolia',
        'flag': 'https://disease.sh/assets/img/flags/mn.png',
        'location': {'lat': 46, 'lng': 105}},
        {'name': 'Montenegro',
        'flag': 'https://disease.sh/assets/img/flags/me.png',
        'location': {'lat': 42, 'lng': 19}},
        {'name': 'Montserrat',
        'flag': 'https://disease.sh/assets/img/flags/ms.png',
        'location': {'lat': 16.75, 'lng': -62.2}},
        {'name': 'Morocco',
        'flag': 'https://disease.sh/assets/img/flags/ma.png',
        'location': {'lat': 32, 'lng': -5}},
        {'name': 'Mozambique',
        'flag': 'https://disease.sh/assets/img/flags/mz.png',
        'location': {'lat': -18.25, 'lng': 35}},
        {'name': 'Myanmar',
        'flag': 'https://disease.sh/assets/img/flags/mm.png',
        'location': {'lat': 22, 'lng': 98}},
        {'name': 'Namibia',
        'flag': 'https://disease.sh/assets/img/flags/na.png',
        'location': {'lat': -22, 'lng': 17}},
        {'name': 'Nepal',
        'flag': 'https://disease.sh/assets/img/flags/np.png',
        'location': {'lat': 28, 'lng': 84}},
        {'name': 'Netherlands',
        'flag': 'https://disease.sh/assets/img/flags/nl.png',
        'location': {'lat': 52.5, 'lng': 5.75}},
        {'name': 'New Caledonia',
        'flag': 'https://disease.sh/assets/img/flags/nc.png',
        'location': {'lat': -21.5, 'lng': 165.5}},
        {'name': 'New Zealand',
        'flag': 'https://disease.sh/assets/img/flags/nz.png',
        'location': {'lat': -41, 'lng': 174}},
        {'name': 'Nicaragua',
        'flag': 'https://disease.sh/assets/img/flags/ni.png',
        'location': {'lat': 13, 'lng': -85}},
        {'name': 'Niger',
        'flag': 'https://disease.sh/assets/img/flags/ne.png',
        'location': {'lat': 16, 'lng': 8}},
        {'name': 'Nigeria',
        'flag': 'https://disease.sh/assets/img/flags/ng.png',
        'location': {'lat': 10, 'lng': 8}},
        {'name': 'Norway',
        'flag': 'https://disease.sh/assets/img/flags/no.png',
        'location': {'lat': 62, 'lng': 10}},
        {'name': 'Oman',
        'flag': 'https://disease.sh/assets/img/flags/om.png',
        'location': {'lat': 21, 'lng': 57}},
        {'name': 'Pakistan',
        'flag': 'https://disease.sh/assets/img/flags/pk.png',
        'location': {'lat': 30, 'lng': 70}},
        {'name': 'Palestine',
        'flag': 'https://disease.sh/assets/img/flags/ps.png',
        'location': {'lat': 32, 'lng': 35.25}},
        {'name': 'Panama',
        'flag': 'https://disease.sh/assets/img/flags/pa.png',
        'location': {'lat': 9, 'lng': -80}},
        {'name': 'Papua New Guinea',
        'flag': 'https://disease.sh/assets/img/flags/pg.png',
        'location': {'lat': -6, 'lng': 147}},
        {'name': 'Paraguay',
        'flag': 'https://disease.sh/assets/img/flags/py.png',
        'location': {'lat': -23, 'lng': -58}},
        {'name': 'Peru',
        'flag': 'https://disease.sh/assets/img/flags/pe.png',
        'location': {'lat': -10, 'lng': -76}},
        {'name': 'Philippines',
        'flag': 'https://disease.sh/assets/img/flags/ph.png',
        'location': {'lat': 13, 'lng': 122}},
        {'name': 'Poland',
        'flag': 'https://disease.sh/assets/img/flags/pl.png',
        'location': {'lat': 52, 'lng': 20}},
        {'name': 'Portugal',
        'flag': 'https://disease.sh/assets/img/flags/pt.png',
        'location': {'lat': 39.5, 'lng': -8}},
        {'name': 'Qatar',
        'flag': 'https://disease.sh/assets/img/flags/qa.png',
        'location': {'lat': 25.5, 'lng': 51.25}},
        {'name': 'Romania',
        'flag': 'https://disease.sh/assets/img/flags/ro.png',
        'location': {'lat': 46, 'lng': 25}},
        {'name': 'Russia',
        'flag': 'https://disease.sh/assets/img/flags/ru.png',
        'location': {'lat': 60, 'lng': 100}},
        {'name': 'Rwanda',
        'flag': 'https://disease.sh/assets/img/flags/rw.png',
        'location': {'lat': -2, 'lng': 30}},
        {'name': 'Réunion',
        'flag': 'https://disease.sh/assets/img/flags/re.png',
        'location': {'lat': -21.1, 'lng': 55.6}},
        {'name': 'S. Korea',
        'flag': 'https://disease.sh/assets/img/flags/kr.png',
        'location': {'lat': 37, 'lng': 127.5}},
        {'name': 'Saint Kitts and Nevis',
        'flag': 'https://disease.sh/assets/img/flags/kn.png',
        'location': {'lat': 17.3333, 'lng': -62.75}},
        {'name': 'Saint Lucia',
        'flag': 'https://disease.sh/assets/img/flags/lc.png',
        'location': {'lat': 13.8833, 'lng': -61.1333}},
        {'name': 'Saint Martin',
        'flag': 'https://disease.sh/assets/img/flags/mf.png',
        'location': {'lat': 18.11, 'lng': -63.03}},
        {'name': 'Saint Pierre Miquelon',
        'flag': 'https://disease.sh/assets/img/flags/pm.png',
        'location': {'lat': 46.8333, 'lng': -56.3333}},
        {'name': 'Saint Vincent and the Grenadines',
        'flag': 'https://disease.sh/assets/img/flags/vc.png',
        'location': {'lat': 13.25, 'lng': -61.2}},
        {'name': 'San Marino',
        'flag': 'https://disease.sh/assets/img/flags/sm.png',
        'location': {'lat': 43.7667, 'lng': 12.4167}},
        {'name': 'Sao Tome and Principe',
        'flag': 'https://disease.sh/assets/img/flags/st.png',
        'location': {'lat': 1, 'lng': 7}},
        {'name': 'Saudi Arabia',
        'flag': 'https://disease.sh/assets/img/flags/sa.png',
        'location': {'lat': 25, 'lng': 45}},
        {'name': 'Senegal',
        'flag': 'https://disease.sh/assets/img/flags/sn.png',
        'location': {'lat': 14, 'lng': -14}},
        {'name': 'Serbia',
        'flag': 'https://disease.sh/assets/img/flags/rs.png',
        'location': {'lat': 44, 'lng': 21}},
        {'name': 'Seychelles',
        'flag': 'https://disease.sh/assets/img/flags/sc.png',
        'location': {'lat': -4.5833, 'lng': 55.6667}},
        {'name': 'Sierra Leone',
        'flag': 'https://disease.sh/assets/img/flags/sl.png',
        'location': {'lat': 8.5, 'lng': -11.5}},
        {'name': 'Singapore',
        'flag': 'https://disease.sh/assets/img/flags/sg.png',
        'location': {'lat': 1.3667, 'lng': 103.8}},
        {'name': 'Sint Maarten',
        'flag': 'https://disease.sh/assets/img/flags/sx.png',
        'location': {'lat': 18.02, 'lng': -63.06}},
        {'name': 'Slovakia',
        'flag': 'https://disease.sh/assets/img/flags/sk.png',
        'location': {'lat': 48.6667, 'lng': 19.5}},
        {'name': 'Slovenia',
        'flag': 'https://disease.sh/assets/img/flags/si.png',
        'location': {'lat': 46, 'lng': 15}},
        {'name': 'Somalia',
        'flag': 'https://disease.sh/assets/img/flags/so.png',
        'location': {'lat': 10, 'lng': 49}},
        {'name': 'South Africa',
        'flag': 'https://disease.sh/assets/img/flags/za.png',
        'location': {'lat': -29, 'lng': 24}},
        {'name': 'South Sudan',
        'flag': 'https://disease.sh/assets/img/flags/ss.png',
        'location': {'lat': 6.8769, 'lng': 31.3069}},
        {'name': 'Spain',
        'flag': 'https://disease.sh/assets/img/flags/es.png',
        'location': {'lat': 40, 'lng': -4}},
        {'name': 'Sri Lanka',
        'flag': 'https://disease.sh/assets/img/flags/lk.png',
        'location': {'lat': 7, 'lng': 81}},
        {'name': 'St. Barth',
        'flag': 'https://disease.sh/assets/img/flags/bl.png',
        'location': {'lat': 17.89, 'lng': -62.82}},
        {'name': 'Sudan',
        'flag': 'https://disease.sh/assets/img/flags/sd.png',
        'location': {'lat': 15, 'lng': 30}},
        {'name': 'Suriname',
        'flag': 'https://disease.sh/assets/img/flags/sr.png',
        'location': {'lat': 4, 'lng': -56}},
        {'name': 'Swaziland',
        'flag': 'https://disease.sh/assets/img/flags/sz.png',
        'location': {'lat': -26.5, 'lng': 31.5}},
        {'name': 'Sweden',
        'flag': 'https://disease.sh/assets/img/flags/se.png',
        'location': {'lat': 62, 'lng': 15}},
        {'name': 'Switzerland',
        'flag': 'https://disease.sh/assets/img/flags/ch.png',
        'location': {'lat': 47, 'lng': 8}},
        {'name': 'Syrian Arab Republic',
        'flag': 'https://disease.sh/assets/img/flags/sy.png',
        'location': {'lat': 35, 'lng': 38}},
        {'name': 'Taiwan',
        'flag': 'https://disease.sh/assets/img/flags/tw.png',
        'location': {'lat': 23.5, 'lng': 121}},
        {'name': 'Tajikistan',
        'flag': 'https://disease.sh/assets/img/flags/tj.png',
        'location': {'lat': 39, 'lng': 71}},
        {'name': 'Tanzania',
        'flag': 'https://disease.sh/assets/img/flags/tz.png',
        'location': {'lat': -6, 'lng': 35}},
        {'name': 'Thailand',
        'flag': 'https://disease.sh/assets/img/flags/th.png',
        'location': {'lat': 15, 'lng': 100}},
        {'name': 'Timor-Leste',
        'flag': 'https://disease.sh/assets/img/flags/tl.png',
        'location': {'lat': -8.55, 'lng': 125.5167}},
        {'name': 'Togo',
        'flag': 'https://disease.sh/assets/img/flags/tg.png',
        'location': {'lat': 8, 'lng': 1.1667}},
        {'name': 'Trinidad and Tobago',
        'flag': 'https://disease.sh/assets/img/flags/tt.png',
        'location': {'lat': 11, 'lng': -61}},
        {'name': 'Tunisia',
        'flag': 'https://disease.sh/assets/img/flags/tn.png',
        'location': {'lat': 34, 'lng': 9}},
        {'name': 'Turkey',
        'flag': 'https://disease.sh/assets/img/flags/tr.png',
        'location': {'lat': 39, 'lng': 35}},
        {'name': 'Turks and Caicos Islands',
        'flag': 'https://disease.sh/assets/img/flags/tc.png',
        'location': {'lat': 21.75, 'lng': -71.5833}},
        {'name': 'UAE',
        'flag': 'https://disease.sh/assets/img/flags/ae.png',
        'location': {'lat': 24, 'lng': 54}},
        {'name': 'UK',
        'flag': 'https://disease.sh/assets/img/flags/gb.png',
        'location': {'lat': 54, 'lng': -2}},
        {'name': 'USA',
        'flag': 'https://disease.sh/assets/img/flags/us.png',
        'location': {'lat': 38, 'lng': -97}},
        {'name': 'Uganda',
        'flag': 'https://disease.sh/assets/img/flags/ug.png',
        'location': {'lat': 1, 'lng': 32}},
        {'name': 'Ukraine',
        'flag': 'https://disease.sh/assets/img/flags/ua.png',
        'location': {'lat': 49, 'lng': 32}},
        {'name': 'Uruguay',
        'flag': 'https://disease.sh/assets/img/flags/uy.png',
        'location': {'lat': -33, 'lng': -56}},
        {'name': 'Uzbekistan',
        'flag': 'https://disease.sh/assets/img/flags/uz.png',
        'location': {'lat': 41, 'lng': 64}},
        {'name': 'Venezuela',
        'flag': 'https://disease.sh/assets/img/flags/ve.png',
        'location': {'lat': 8, 'lng': -66}},
        {'name': 'Vietnam',
        'flag': 'https://disease.sh/assets/img/flags/vn.png',
        'location': {'lat': 21, 'lng': 105.8}},
        {'name': 'Western Sahara',
        'flag': 'https://disease.sh/assets/img/flags/eh.png',
        'location': {'lat': 24.5, 'lng': -13}},
        {'name': 'Yemen',
        'flag': 'https://disease.sh/assets/img/flags/ye.png',
        'location': {'lat': 15, 'lng': 48}},
        {'name': 'Zambia',
        'flag': 'https://disease.sh/assets/img/flags/zm.png',
        'location': {'lat': -15, 'lng': 30}},
        {'name': 'Zimbabwe',
        'flag': 'https://disease.sh/assets/img/flags/zw.png',
        'location': {'lat': -20, 'lng': 30}}
    ]
    return HttpResponse(json.dumps(data))