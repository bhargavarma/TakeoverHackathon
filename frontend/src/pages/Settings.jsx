export default function Settings(){

return(

<div>

<h1 className="text-4xl font-bold mb-8">

Settings

</h1>

<div className="grid grid-cols-2 gap-6">

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-semibold">

Daily Report

</h2>

<p className="mt-3 text-gray-400">

Daily executive email is enabled.

</p>

</div>

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-semibold">

AI Monitoring

</h2>

<p className="mt-3 text-gray-400">

Inventory monitoring is active.

</p>

</div>

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-semibold">

Auto Procurement

</h2>

<p className="mt-3 text-gray-400">

Requires manual approval.

</p>

</div>

<div className="rounded-3xl bg-white/5 border border-white/10 p-8">

<h2 className="text-2xl font-semibold">

Email

</h2>

<p className="mt-3 text-gray-400">

SMTP Connected

</p>

</div>

</div>

</div>

)

}