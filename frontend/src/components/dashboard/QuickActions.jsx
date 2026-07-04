import { Sparkles,Boxes,ShoppingCart } from "lucide-react";

export default function QuickActions(){

const buttons=[

["Run Daily Review",Sparkles],

["Inventory Scan",Boxes],

["Generate PO",ShoppingCart],

];

return(

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-bold mb-6">

Quick Actions

</h2>

<div className="space-y-4">

{buttons.map(([title,Icon])=>(

<button
key={title}
className="w-full rounded-2xl bg-white/5 hover:bg-violet-600 transition p-5 flex items-center gap-4">

<Icon/>

{title}

</button>

))}

</div>

</div>

)

}